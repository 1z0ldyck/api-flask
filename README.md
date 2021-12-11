comando pra rodar no docker-compose: docker-compose -f docker-compose.yml --build app postgresql

TODO:

- RabbitMQ
- OpenTelemetry
- Grafana
- Prometheus

ENDPOINT /post_person METHOD POST
Example:
  ```{
    "TABLE_NAME_1": {
      "COLUMN_1": "VALUE_1",
      "COLUMN_2:  "VALUE_2"
    },
      "TABLE_NAME_2": {
      "COLUMN_1": "VALUE_1",
      "COLUMN_2:  "VALUE_2"
    }
  }```
 
 Accept more of one table in same post
 Example:
   ```{
    "TABLE_NAME_1": {
      "COLUMN_1": "VALUE_1",
      "COLUMN_2:  "VALUE_2"
    },
      "TABLE_NAME_2": {
      "COLUMN_1": "VALUE_1",
      "COLUMN_2:  "VALUE_2"
    }
  }```
