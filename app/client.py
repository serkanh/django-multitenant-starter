from app.models import Client

# create your public tenant
tenant = Client(domain_url='localhost', # don't add your port or www here! on a local server you'll want to use localhost here
                schema_name='public',
                name='Schemas Inc.',
                paid_until='2016-12-05',
                on_trial=False)
tenant.save()
