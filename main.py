import json
import schedule
import time


class GrowingProgram(object):
    growing_programs = {}

    def parse_growing_json(self, data_JSON):
        growing_program = {}
        blocks = []
        ser_data = json.loads(data_JSON)
        for key, value in ser_data.items():
            if key != "blocks":
                growing_program[key] = value
            if key == "blocks":
                for element in value:
                    blocks.append(element)
        growing_program["blocks"] = blocks
        return growing_program

    def add_new_growing_program(self, data_JSON):
        dict_growing_program = self.parse_growing_JSON(data_JSON)
        value_id = dict_growing_program.pop("id")
        self.growing_programs[value_id] = dict_growing_program
        print(self.growing_programs)

    def start_growing_program(self, dict_growing_program):
        counter_days = 0

        for element in dict_growing_program["blocks"]:
            days = element["blockDays"]
            counter_days += days
            schedule.every(counter_days).seconds.do(self.stop_shedule, name='task_' + str(counter_days)).tag(
                'task_' + str(counter_days))

    def stop_growing_program(self):
        pass

    def pause_growing_program(self):
        pass

    def stop_shedule(self, name):
        print("Этап " + name + " завершен")
        schedule.clear(name)


if __name__ == "__main__":
    data_JSON = '{ "id":"1", "programName":"GrowingProgram1","groups":"Sensor1", "days":"30", "status":"start", "blocks":[ { "id":"1", "blockDays":10, "airTemperature":"1234", "waterTemperature":"1234", "airHumidity":"1234", "waterHumidity":"1234", "lightPeriod":"1234" }, { "id":2, "blockDays":20, "airTemperature":"1234", "waterTemperature":"1234", "airHumidity":"1234", "waterHumidity":"1234", "lightPeriod":"1234" }, { "id":"3", "blockDays":30, "airTemperature":"1234", "waterTemperature":"1234", "airHumidity":"1234", "waterHumidity":"1234", "lightPeriod":"1234"} ]}'

    growing_program_class = GrowingProgram()

    #dict_growing_program = growing_program_class.parse_growing_JSON(data_JSON)

    #growing_program_class.start_growing_program(dict_growing_program)

    growing_program_class.add_new_growing_program(data_JSON)

    while True:
        schedule.run_pending()
        time.sleep(1)




