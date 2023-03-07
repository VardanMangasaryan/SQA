import pytest
from pom.pages.navigation_panel import NavigationPanel


@pytest.mark.usefixtures("log_in")
class TestNavigationPanel:

    def test_recruitment_page(self):
        """Test is not complete"""
        navigation_panel = NavigationPanel(self.driver)
        navigation_panel.wait_for_page_load()
        navigation_panel.go_to("Recruitment")



