from reactpy import component, run
import reactpy_material as rp_m

@component
def app():
    return rp_m.container(
        rp_m.accordion(
            rp_m.accordion_summary("Accordion 1"),
            rp_m.accordion_details(
                '''
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                malesuada lacus ex, sit amet blandit leo lobortis eget.
                '''
            )
        )
    )

run(app)