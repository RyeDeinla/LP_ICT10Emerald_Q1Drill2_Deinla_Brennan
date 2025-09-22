from pyscript import document 

def string_showcase(event):
    #Get the input value
    input1 = str(document.getElementById("name").value)
    input2 = str(document.getElementById("age").value)
    input3 = str(document.getElementById("school").value)

    #Compile the input values
    compilation = input1 + " " + "is currently" + " " + input2 + " " + "years old and studies at" + " " + input3 + "." + " " + """This information was gathered through input fields and displayed using
    a multiline string in Python via PyScript."""

    #Displaying the results
    document.getElementById("notes").innerText = compilation
    document.getElementById("name2").innerText = input1
    document.getElementById("age2").innerText = input2
    document.getElementById("school2").innerText = input3
    