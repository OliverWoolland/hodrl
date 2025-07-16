import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

def create_accordion_item(label, icon_name, colour_key, value):
    return dmc.AccordionItem(
        [
            dmc.AccordionControl(
                label,
                icon=DashIconify(
                    icon=icon_name,
                    color=dmc.DEFAULT_THEME["colors"][colour_key][6],
                    width=20,
                ),
            ),
            dmc.AccordionPanel(value),
        ],
        value=value,
    )
 
def get_main_accordion():
    items = [
        ("Assets", "bi:file-text", "blue", "No assets found"),
        ("Policies", "bi-card-checklist", "red", "No policies found"),
        ("Constraints", "tabler:circle-check", "green", "No contstraints found"),
        ("Rules", "bi:sign-stop", "pink", "No rules found"),
    ]
    
    return dmc.Accordion(
        disableChevronRotation=True,
        value=[item[3] for item in items], # open all times by default
        children=[create_accordion_item(*item) for item in items], # add items
    )
