import sys

args = sys.argv[1:]

if args and (len(args) == 2):
    appname, gitrepo = args
else:
    appname = raw_input('What is the application name? ')
    gitrepo = raw_input('Where is the git repo? ')

print "Creating %s-install.sh for:" % appname
print "appname: %s" % appname
print "git repo: %s" % gitrepo

template = open('install.template', 'r').read()
template = template.replace('{{ appname }}', appname)
template = template.replace('{{ gitrepo }}', gitrepo)

script = open('%s-install.sh' % appname, 'w')
script.write(template)
