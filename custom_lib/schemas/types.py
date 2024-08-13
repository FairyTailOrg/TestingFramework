
class Scheduling:
    def __init__(self):
        pass

    def appt_reasons(self):
        return {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title": "Generated schema for Root",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                "paAppointmentReasonId": {
                    "type": "number"
                },
                "isNewPatient": {
                    "type": "boolean"
                },
                "appointmentReason": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "userExperience": {
                    "type": "string"
                },
                "ahAppointmentTypes": {
                    "type": "array",
                    "items": {
                    "type": "object",
                    "properties": {
                        "ahAppointmentTypeId": {
                        "type": "number"
                        },
                        "appointmentTypeId": {
                        "type": "number"
                        },
                        "practiceId": {
                        "type": "number"
                        },
                        "name": {
                        "type": "string"
                        },
                        "shortname": {
                        "type": "string"
                        },
                        "isTelehealth": {
                        "type": "boolean"
                        }
                    },
                    "required": [
                        "ahAppointmentTypeId",
                        "appointmentTypeId",
                        "practiceId",
                        "name",
                        "shortname",
                        "isTelehealth"
                    ]
                    }
                },
                "patientBookingNote": {
                    "type": "string"
                },
                "paAppointmentTypeId": {
                    "type": "number"
                }
                },
                "required": [
                "paAppointmentReasonId",
                "isNewPatient",
                "appointmentReason",
                "description",
                "userExperience",
                "ahAppointmentTypes",
                "patientBookingNote",
                "paAppointmentTypeId"
                ]
            }
            }