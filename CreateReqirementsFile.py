# run this file to create a requirements.txt file
# or
# run this command in the terminal or cmd : pip freeze > requirements.txt

import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
file = open("requirements.txt", "w")
data = "\n".join(installed_packages_list)
file.write(data)
file.close()
