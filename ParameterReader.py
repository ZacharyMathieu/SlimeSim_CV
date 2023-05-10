from InputParam import InputParam
import Constants


class ParameterReader:
    @staticmethod
    def read(file_name: str) -> list[InputParam]:
        delimiter = Constants.PARAMETER_DELIMITER

        p_list = []
        path = "./{fileName}".format(fileName=file_name)

        try:
            file = open(path)
            while True:
                line = file.readline()

                if line == "":
                    break

                out = line.split(delimiter)

                if len(out) >= 2:
                    param = InputParam()
                    param.name = out[0]
                    try:
                        float_value = float(out[1])
                        param.value_number = float_value
                    except ValueError:
                        bool_value = True if out[1].lower() in Constants.PARAMETER_TRUE_VALUES \
                            else False if out[1].lower() in Constants.PARAMETER_FALSE_VALUES \
                            else None
                        if bool_value is not None:
                            param.value_bool = bool_value
                        else:
                            param.value_string = out[1]

                    p_list.append(param)

            file.close()
        except FileNotFoundError:
            print("FILE FAILED TO OPEN: [{}]\n".format(path))

        return p_list
