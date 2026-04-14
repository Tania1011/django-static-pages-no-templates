from django.http import HttpResponse
#GLOBAL DATA 
# Variables
site_name = "My Django Website"
year = 2026
rating = 4.8

# 6 mixed types: string, int, float, bool, None, dict
my_list = ["Django", 100, 3.14, True, None, {"language": "Python"}]

# Dictionary ( 5 keys, mixed types)
site_info = {
    "email": "support@example.com",   # string
    "version": 1.0,                   # float
    "users": 1500,                   # int
    "active": True,                  # boolean
    "owner": "Tatiana"               # string
}

pages = ["Home", "Contact", "About", "Help", "Subscribe"]

nav = """
    <nav>
        <a href='/'>Home</a> |
        <a href='/contact/'>Contact</a> |
        <a href='/about/'>About</a> |
        <a href='/help/'>Help</a> |
        <a href='/subscribe/'>Subscribe</a>
    </nav>
"""

home_body = f"""
<ol>
    <li>Site Name: {site_name}</li>
    <li>Year Created: {year}</li>
    <li>User Rating: {rating:.2f}</li>
</ol>
"""
 
    
def home(request):
    content = f"""
    {nav}
    <h1>Welcome to {site_name}</h1>
    <p>Author: {site_info['owner']}</p>
    <h2>Pages</h2>
    <ul>
        {"".join([f"<li>{p}</li>" for p in pages])}
    </ul>
    <h2>List</h2>
    <ul>
        {"".join([f"<li>{i}</li>" for i in my_list])}
    </ul>
    <h2>Site Info</h2>
    <ul>
        <li>Email: {site_info['email']}</li>
        <li>Version: {site_info['version']}</li>
        <li>Users: {site_info['users']}</li>
        <li>Active: {site_info['active']}</li>
        <li>Owner: {site_info['owner']}</li>
    </ul>
    """
    return HttpResponse(content)  

def contact(request):
    email = site_info.get('email', 'Not available')
    
    content = f"""
    <h1>Contact Page</h1>
    <h2>Get in touch with us</h2>
    <p>Email: {email}</p>
    """
    return HttpResponse(nav + content)

def about(request):
    content = f"""
    <h1>About Page</h1>
    <h2>About this project</h2>
    <p>This is the about page.</p>
    <p>Author: {site_info['owner']}</p>
    """
    return HttpResponse(nav + content)

def help(request):
    content = f"""
    <h1>Help Page</h1>
    <h2>Support Center</h2>
    <p>Need help? Contact support.</p>
    """
    return HttpResponse(nav + content)

def subscribe(request):
    content = f"""
    <h1>Subscribe Page</h1>
    <h2>Join Us</h2>
    <p>Stay updated with {site_name}</p>
    """
    return HttpResponse(nav + content)





