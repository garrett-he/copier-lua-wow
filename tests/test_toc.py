"""Integration tests for {project_name}.toc generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_toc_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that {project_name}.toc is generated with correct filename."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    toc = result.project_dir / f'{base_answers["project_name"]}.toc'
    assert toc.exists(), f'{base_answers["project_name"]}.toc file not found'

    content = toc.read_text()
    assert f'## Title: {base_answers["project_name"]}' in content


def test_toc_interface(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that TOC contains correct Interface version."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    toc = result.project_dir / f'{base_answers["project_name"]}.toc'
    content = toc.read_text()
    assert '## Interface: 120005' in content


def test_toc_description(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that TOC contains project_description."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    toc = result.project_dir / f'{base_answers["project_name"]}.toc'
    content = toc.read_text()
    assert f'## Notes: {base_answers["project_description"]}' in content


def test_toc_author(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that TOC contains copyright_holder_name and email."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    toc = result.project_dir / f'{base_answers["project_name"]}.toc'
    content = toc.read_text()
    assert f'## Author: {base_answers["copyright_holder_name"]}' in content
    assert f'<{base_answers["copyright_holder_email"]}>' in content


def test_toc_version(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that TOC contains project_version."""
    answers = {**base_answers, 'project_version': '1.2.3'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    toc = result.project_dir / f'{base_answers["project_name"]}.toc'
    content = toc.read_text()
    assert '## Version: 1.2.3' in content


def test_toc_main_lua(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that TOC references main.lua."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    toc = result.project_dir / f'{base_answers["project_name"]}.toc'
    content = toc.read_text()
    assert 'main.lua' in content
