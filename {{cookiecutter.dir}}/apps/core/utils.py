def create_employee_code(self, model):
    initial_name = self.user.first_name + self.user.last_name
    client_code = ""

    for i in initial_name.upper().split():
        client_code += i[0]

    last_in = model.objects.all().order_by("id").last()

    if not last_in:
        seq = 0
        client_code = client_code + "000" + str(int(seq) + 1)
        return client_code

    if self.id:
        client_code = client_code + "000" + str(self.id)
        return client_code

    in_id = last_in.id
    in_int = int(in_id)

    client_code = client_code + "000" + str(int(in_int) + 1)
    return client_code
