class user:
    def _init_(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def user_show(self):
        print("User's id: ",self.id,"; User's Name: ",self.name,"; User's Salary: ",self.salary)



class project:

    def _init_(self,id, name, users):
        self.id=id
        self.name=name
        self.users=users

    def sort_users(self):
        for i in range(len(self.users)):
            for j in range(len(self.users)-i-1):
                if(self.users[j].salary<self.users[j+1].salary):
                    self.users[j],self.users[j+1]=self.users[j+1],self.users[j]


    def show_project(self):
        print("Project Details----->")
        print("Project Id: ",self.id)
        print("Project name: ",self.name)
        print("Project Participants:-")
        [i.user_show() for i in self.users]

    @staticmethod
    def sort_proj_users(proj_list):
        [i.sort_users() for i in proj_list]

        return proj_list

    @staticmethod
    def proj_sort(proj_list):
        [i.sort_users() for i in proj_list]
        for i in range(len(proj_list)):
            for j in range(len(proj_list) - i - 1):
                if(proj_list[j].users[0].salary < proj_list[j+1].users[0].salary):
                    proj_list[j], proj_list[j + 1] = proj_list[j + 1], proj_list[j]

        return proj_list

    @staticmethod
    def show_all_projects(proj_list):
        [i.show_project() for i in proj_list]

    @staticmethod
    def create_dict(proj_list):

        d={i.id:i for i in proj_list}

        return d

projects=[project(1,"The Office1",[user(4,"Jim Halpert",5000),user(1,"Bob Vance",10000),user(3,"Micheal Scott",7000)]),
    project(2, "The Office2", [user(5, "Dwight Schrute", 5000), user(6, "Pam Beasly", 3000), user(2, "David Wallace", 15000)]),
    project(3, "The Office3", [user(7, "Andy Bernardt", 5000), user(8, "Creed Branton", 2000), user(9, "Toby Fergusan", 6000)])]

print("All Projects ")
project.show_all_projects(projects)


print("\n\nPart 1 : Project with sorted users ")
projects=project.sort_proj_users(projects)
project.show_all_projects(projects)

print("\n\nPart 2: All Sorted Projects")
projects=project.proj_sort(projects)
project.show_all_projects(projects)

print("\n\nPart 2: Dictionary of all the projects")
proj_dict = project.create_dict(projects)
print(proj_dict)
