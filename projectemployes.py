class user:
    def _init_(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.designation=desig
        self.salary=salary
        self.message="UTILISED"

    def set_msg(self, msg):
        self.message=msg

    def is_equal(self,us):
        return self.id==us.id and self.name==us.name and self.salary==us.salary

    def user_show(self):
        print("User's id: ",self.id,"; User's Name: ",self.name,"; User's Designation : ",self.designation,"; User's Salary: ",self.salary)

    def show_utilisation(self):
        print("User's id: ",self.id,"; Name: ",self.name,"; Utilisation: ",self.message)

    @staticmethod
    def get_emp_list(proj_list):
        all_users=set()
        for i in proj_list:
            for j in i.users:
                all_users.add(j)

        users_dict=dict()
        users_dict_id=dict()
        for i in all_users:
            lists_of_projects=[]
            for j in proj_list:
                for k in j.users:
                    if i.is_equal(k):
                        lists_of_projects.append(j)
            #print(lists_of_projects)
            users_dict_id[i.id]=lists_of_projects
            users_dict[i]=lists_of_projects

        return users_dict_id,users_dict

    @staticmethod
    def calculate_efforts_set_msg(users_dict):

        for i in users_dict.items():
            total_efforts=0
            for j in i[1]:
                total_efforts+=j.efforts

            if(total_efforts>100):
                i[0].set_msg("OVER UTILISED")
            elif(total_efforts<50):
                i[0].set_msg("UNDER UTILISED")

        return users_dict






class project:

    def _init_(self,id, name,efforts, users):
        self.id=id
        self.name=name
        self.efforts=efforts
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


projects=[project(1,"The Office1",20,[user(4,"Jim Halpert","Asst Regional Manager",5000),user(1,"Bob Vance","COO",10000),user(3,"Micheal Scott","Manager",7000)]),
    project(2, "The Office2", 30,[user(3,"Micheal Scott","Manager",7000), user(6, "Pam Beasly","Receptionist", 3000), user(2, "David Wallace","CEO" ,15000)]),
    project(3, "The Office3", 40,[user(6, "Pam Beasly","Receptionist",3000), user(3,"Micheal Scott","Manager",7000), user(9, "Toby Fergusan","HR",6000)])]


Users_Dict_id,Users_Dict=user.get_emp_list(projects)


print("List of Projects every employee has *****>")
for i in Users_Dict_id.items():
    print("\n\nUser Id : ",i[0])
    print("<======== All the projects related to this employee ========>")
    [j.show_project() for j in i[1]]
    print("<======== ========================================= ========>")

Users_Dict=user.calculate_efforts_set_msg(Users_Dict)

print("\n\n\nSee the utilisation of every employee *****>")
for i in Users_Dict.keys():
    i.show_utilisation()
