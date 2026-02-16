"""Integration tests for modules/example.lua generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_example_module_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that modules/example.lua is generated with correct project_name."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    example_module = result.project_dir / 'modules' / 'example.lua'
    assert example_module.exists(), 'modules/example.lua file not found'

    content = example_module.read_text()
    assert f'local _, {base_answers["project_name"]} = ...' in content
    assert f'{base_answers["project_name"]}.example = {{}}' in content


def test_example_module_foo_function(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that example module contains foo function."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    example_module = result.project_dir / 'modules' / 'example.lua'
    content = example_module.read_text()
    assert f'{base_answers["project_name"]}.example.foo = function ()' in content
    assert f'return "Function {base_answers["project_name"]}.example.foo invoked."' in content
