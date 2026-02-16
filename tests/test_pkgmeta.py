"""Integration tests for .pkgmeta generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_pkgmeta_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that .pkgmeta is generated with correct package-as."""
    answers = {**base_answers, 'with_changelog': False}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    pkgmeta = result.project_dir / '.pkgmeta'
    assert pkgmeta.exists(), '.pkgmeta file not found'

    content = pkgmeta.read_text()
    assert f'package-as: {answers["project_name"]}' in content
    assert 'enable-nolib-creation: yes' in content


def test_pkgmeta_with_changelog(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that .pkgmeta includes manual-changelog when with_changelog is True."""
    answers = {**base_answers, 'with_changelog': True}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pkgmeta = result.project_dir / '.pkgmeta'
    assert pkgmeta.exists()

    content = pkgmeta.read_text()
    assert 'manual-changelog:' in content
    assert 'filename: CHANGELOG.md' in content
    assert 'markup-type: markdown' in content


def test_pkgmeta_without_changelog(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that .pkgmeta excludes manual-changelog when with_changelog is False."""
    answers = {**base_answers, 'with_changelog': False}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pkgmeta = result.project_dir / '.pkgmeta'
    assert pkgmeta.exists()

    content = pkgmeta.read_text()
    assert 'manual-changelog' not in content


def test_pkgmeta_ignore_entries(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that .pkgmeta contains standard ignore entries."""
    answers = {**base_answers, 'with_changelog': False}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pkgmeta = result.project_dir / '.pkgmeta'
    content = pkgmeta.read_text()
    assert '.git*' in content
    assert '.pkgmeta' in content
    assert '.*ignore' in content
