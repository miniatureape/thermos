appname = raw_input('What is the application name?')
gitrepo = raw_input('Where is the git repo?')

print "Creating script for:"
print "appname: %s" % appname
print "git repo: %s" % gitrepo

template = open('install.template', 'r').read()
template = template.replace('{{ appname }}', appname)
template = template.replace('{{ gitrepo }}', gitrepo)

script = open('install.sh', 'w')
script.write(template)
