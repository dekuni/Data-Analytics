"""
Test suite for the COVID-19 PNAD Analysis Streamlit application.

This test suite validates the basic structure and functionality of the Streamlit app
including data loading, UI components, and code execution paths.
"""

import pytest
from pathlib import Path
from PIL import Image
import sys


class TestAppStructure:
    """Tests for the basic structure of the application"""
    
    def test_app_file_exists(self):
        """Test that app.py exists"""
        assert Path('app.py').exists(), "app.py file should exist"
    
    def test_required_images_exist(self):
        """Test that all required image files exist"""
        required_images = [
            'caracteristica_populacao_1.jpg',
            'caracteristica_populacao_2.jpg',
            'caracteristica_populacao_3.jpg',
            'caracteristica_populacao_4.jpg',
            'dados_socioeconomicos_1.jpg',
            'dados_socioeconomicos_2.jpg',
            'dados_socioeconomicos_3.jpg',
            'dados_socioeconomicos_4.jpg',
            'sintomas_1.jpg',
            'sintomas_2.jpg',
            'sintomas_3.jpg',
            'sintomas_4.jpg',
        ]
        
        for image_file in required_images:
            assert Path(image_file).exists(), f"Image {image_file} should exist"
    
    def test_images_are_valid(self):
        """Test that image files can be opened and are valid"""
        image_files = [f for f in Path('.').glob('*.jpg')]
        
        for image_file in image_files:
            try:
                img = Image.open(image_file)
                assert img.size[0] > 0 and img.size[1] > 0, f"Image {image_file} should have valid dimensions"
            except Exception as e:
                pytest.fail(f"Failed to open image {image_file}: {e}")
    
    def test_colab_directory_exists(self):
        """Test that the Colab directory with CSV files exists"""
        colab_dir = Path('Colab')
        assert colab_dir.exists(), "Colab directory should exist"
        assert colab_dir.is_dir(), "Colab should be a directory"


class TestAppImports:
    """Tests for application imports and dependencies"""
    
    def test_streamlit_import(self):
        """Test that streamlit can be imported"""
        try:
            import streamlit
            assert True
        except ImportError:
            pytest.fail("streamlit package should be importable")
    
    def test_pil_import(self):
        """Test that PIL can be imported"""
        try:
            from PIL import Image
            assert True
        except ImportError:
            pytest.fail("PIL package should be importable")
    
    def test_time_import(self):
        """Test that time module can be imported"""
        try:
            import time
            assert True
        except ImportError:
            pytest.fail("time module should be importable")


class TestAppContent:
    """Tests for app.py content and structure"""
    
    def test_app_contains_title(self):
        """Test that app.py contains a title"""
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert 'st.title' in content, "App should contain a title"
        assert 'PNAD' in content, "App should reference PNAD in content"
    
    def test_app_contains_tabs(self):
        """Test that app.py contains tab structure"""
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert 'st.tabs' in content, "App should use tabs"
        assert 'Introdução' in content, "App should have Introduction tab"
        assert 'Análise dos Dados' in content, "App should have Data Analysis tab"
        assert 'Conclusão' in content, "App should have Conclusion tab"
    
    def test_app_contains_sql_queries(self):
        """Test that app.py contains SQL query examples"""
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert 'st.code' in content, "App should display code blocks"
        assert 'SELECT' in content, "App should contain SQL SELECT statements"
        assert 'FROM' in content, "App should contain SQL FROM statements"
    
    def test_app_contains_image_display(self):
        """Test that app.py contains image display functionality"""
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert 'Image.open' in content, "App should open images"
        assert 'st.image' in content, "App should display images"
    
    def test_app_contains_buttons(self):
        """Test that app.py contains interactive buttons"""
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert 'st.button' in content, "App should have buttons"
        assert 'Gráfico' in content or 'Query' in content, "App should have graph/query buttons"
    
    def test_app_contains_spinner(self):
        """Test that app.py uses spinners for loading states"""
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert 'st.spinner' in content, "App should use spinners for loading"
        assert 'Carregando' in content, "App should have loading messages"


class TestDataStructure:
    """Tests for data structure and organization"""
    
    def test_csv_files_exist(self):
        """Test that expected CSV files exist in Colab directory"""
        colab_dir = Path('Colab')
        
        if colab_dir.exists():
            csv_files = list(colab_dir.glob('*.csv'))
            assert len(csv_files) > 0, "Colab directory should contain CSV files"
    
    def test_readme_exists(self):
        """Test that README.md exists"""
        assert Path('README.md').exists(), "README.md should exist"
    
    def test_readme_not_empty(self):
        """Test that README.md is not empty"""
        readme = Path('README.md')
        if readme.exists():
            content = readme.read_text()
            assert len(content) > 0, "README.md should not be empty"


class TestAppConfiguration:
    """Tests for Streamlit configuration"""
    
    def test_app_page_config(self):
        """Test that app configures page settings"""
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert 'st.set_page_config' in content, "App should set page configuration"
    
    def test_app_has_dividers(self):
        """Test that app uses dividers for visual separation"""
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert 'st.divider' in content, "App should use dividers for sections"
    
    def test_app_has_headers(self):
        """Test that app uses headers for organization"""
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert 'st.header' in content or 'st.title' in content, "App should use headers"


class TestSyntax:
    """Tests for Python syntax and basic validation"""
    
    def test_app_syntax_valid(self):
        """Test that app.py has valid Python syntax"""
        try:
            with open('app.py', 'r', encoding='utf-8') as f:
                compile(f.read(), 'app.py', 'exec')
            assert True
        except SyntaxError as e:
            pytest.fail(f"app.py has syntax error: {e}")
    
    def test_app_no_obvious_errors(self):
        """Test that app.py can be imported without errors (basic check)"""
        # This is a basic check - full app execution would require Streamlit runtime
        with open('app.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for common errors
        assert content.count('(') == content.count(')'), "Parentheses should be balanced"
        assert content.count('[') == content.count(']'), "Brackets should be balanced"
        assert content.count('{') == content.count('}'), "Braces should be balanced"


# Run tests with verbose output if executed directly
if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
