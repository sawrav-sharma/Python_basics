def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")

    return nowexec


@dec1
def who_m_i():
    print("Myself Jacob")


who_m_i()
