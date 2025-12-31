from .models import Category
# File ka naam context_processors.py rakha ajta hai , Reason. :Future me easily find ho,Team ko samajh aaye
# ek function hota hai jo: Har template request par automatically run hota hai
#                            Ye function database se sari categories nikal kar
#                              template ko bhej deta hai taake menu / navbar me show ho saken.
def menu_links(request):
    links = Category.objects.all() # fetch all categories from the Database [shose, pants,shirts]
    return dict(links=links)      #Ye data template me jata hai:: links  →  [Electronics, Clothes, Shoes]
                                # incluging also in setting.py on line 67
            #              Django kehta hai:
#“HTML ko ek variable do jiska naam links ho aur usme categories hon.”