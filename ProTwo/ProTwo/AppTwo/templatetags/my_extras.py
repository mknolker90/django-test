from django import template



def cut(value,arg):

    """
    this filter eliminates arg from string
    """

    return value.replace(arg,'')

register=template.library
#register.filter('cut',cut)

##  check 
