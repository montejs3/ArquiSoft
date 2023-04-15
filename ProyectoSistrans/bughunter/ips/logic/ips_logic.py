
from ..models import Ips

def get_ipss():
    queryset = Ips.objects.all()
    return queryset



def create_ips(form):
    ips = form.save()
    ips.save()
    return ()