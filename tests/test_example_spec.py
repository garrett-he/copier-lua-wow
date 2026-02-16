"""Integration tests for spec/example_spec.lua generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_example_spec_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that spec/example_spec.lua is generated with correct project_name."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    example_spec = result.project_dir / 'spec' / 'example_spec.lua'
    assert example_spec.exists(), 'spec/example_spec.lua file not found'

    content = example_spec.read_text()
    assert 'require("spec.helper")' in content
    assert f'local {base_answers["project_name"]} = {{}}' in content


def test_example_spec_loadchunk(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that example_spec uses loadchunk with correct project_name."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    example_spec = result.project_dir / 'spec' / 'example_spec.lua'
    content = example_spec.read_text()
    assert f'loadchunk({base_answers["project_name"]}, "modules/example")' in content


def test_example_spec_describe(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that example_spec contains correct describe blocks."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    example_spec = result.project_dir / 'spec' / 'example_spec.lua'
    content = example_spec.read_text()
    assert f'describe("Module {base_answers["project_name"]}.example"' in content
    assert 'describe("Function foo()"' in content
    assert 'it("should be invoked."' in content


def test_example_spec_assertion(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that example_spec assertion uses correct project_name."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    example_spec = result.project_dir / 'spec' / 'example_spec.lua'
    content = example_spec.read_text()
    expected = f'"Function {base_answers["project_name"]}.example.foo invoked."'
    assert expected in content
