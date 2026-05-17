# Ejercicio 9 - Combinar dos archivos


def merge_files(file1, file2, output):
    try:
        with open(file1, 'r') as f1:
            with open(file2, 'r') as f2:

                content1 = f1.read()
                content2 = f2.read()

                with open(output, 'w') as f_out:
                    f_out.write(content1)
                    f_out.write(content2)

    except FileNotFoundError:
        raise
