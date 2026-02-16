"""Integration tests for spec/helper.lua generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_helper_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that spec/helper.lua is generated with correct project_name."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    helper = result.project_dir / 'spec' / 'helper.lua'
    assert helper.exists(), 'spec/helper.lua file not found'

    content = helper.read_text()
    assert 'function loadchunk(t, path)' in content


def test_helper_loadchunk(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that helper loadchunk function uses correct project_name."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    helper = result.project_dir / 'spec' / 'helper.lua'
    content = helper.read_text()
    assert f'chunk("{base_answers["project_name"]}", t)' in content
