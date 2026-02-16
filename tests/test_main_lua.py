"""Integration tests for main.lua generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_main_lua_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that main.lua is generated with correct project_name."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    main_lua = result.project_dir / 'main.lua'
    assert main_lua.exists(), 'main.lua file not found'

    content = main_lua.read_text()
    assert f'local _, {base_answers["project_name"]} = ...' in content


def test_main_lua_content(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that main.lua contains the addon initialization pattern."""
    answers = {**base_answers, 'project_name': 'my-addon'}
    result = copie.copy(extra_answers=answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    main_lua = result.project_dir / 'main.lua'
    content = main_lua.read_text()
    assert 'local _, my-addon = ...' in content
