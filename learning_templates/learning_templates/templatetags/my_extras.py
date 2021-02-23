from django import template
register=template.library()
def cut(value,args):
    return value.replace(arg,'')
register.filter('cut',cut)
# string,function    
