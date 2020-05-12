"""First test."""


def test_application(app):
    selectors = {"control_type": "MenuItem", "title_re": "Reporting"}
    app.find_element(selectors).click()
