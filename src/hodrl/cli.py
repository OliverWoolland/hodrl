import click
from hodrl import asset_queries

# ------------------------------------------------------------------------------
# Click groups 

@click.group()
def click_entrypoint():
    """ Root command group """
    pass

@click_entrypoint.group()
def asset():
    """ Command group for managing assets """
    pass

# ------------------------------------------------------------------------------
# Click commands

@asset.command(name="ls")
def asset_list_all():
    result = asset_queries.get_all_assets()
    return result

# ------------------------------------------------------------------------------
# Python entrypoint

def main():
    click_entrypoint() 

if __name__ == "__main__":
    main()
