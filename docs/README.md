

### TODO:

- RabbitMQ
- OpenTelemetry
- Grafana
- Prometheus

### ENDPOINT /post_person -> METHOD POST

  ```
  {
    "TABLE_NAME_1": {
      "COLUMN_1": "VALUE_1",
      "COLUMN_2:  "VALUE_2"
    }
  }
 
 Accept more of one table in same post
 Example:
 {
    "TABLE_NAME_1": {
      "COLUMN_1": "VALUE_1",
      "COLUMN_2:  "VALUE_2"
    },
    "TABLE_NAME_2": {
      "COLUMN_1": "VALUE_1",
      "COLUMN_2:  "VALUE_2"
    }
 }
 
```