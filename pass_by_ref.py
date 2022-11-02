# Here it is implemented how pass by Reference works
# 1.when a customer object is created, a variable here(cus_obj_ref) accept obj's address
# and it redirect to that address
# 2. when function here guess() is passed (cus_obj_ref) <at line no.2>5 which is a reference pointer of obj's address
# 3.So, below both variable => cus_obj_ref and cus_obj_ref_2 point the same address point
# 4.if one of them update the point obj's properties then both of them will affected
# And that is, pass by ref.
# <Note> class's bojetcs are mutable like list,dic,set


class Customer:
    def __init__(self, name):
        self.name = name


def guess(cus_obj_ref_2):
    print("Guess fun => cus_obj_id : ", id(cus_obj_ref_2))
    print("Guess fun => cus_obj_name : ", cus_obj_ref_2.name)

    cus_obj.name = "ABB"
    print("Guess fun => cus_obj_name_updated : ", cus_obj_ref_2.name)


cus_obj_ref = Customer("BoBo")
print("Main code => cus_obj_id : ", id(cus_obj_ref))
print("Main code => cus_obj_name : ", cus_obj_ref.name)


guess(cus_obj_ref)


print("Main code => cus_obj_name again : ", cus_obj_ref.name)
