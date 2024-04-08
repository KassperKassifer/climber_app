<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
    mermaid.initialize({ startOnLoad: true });
</script>
```mermaid
classDiagram
    class Gym {
        + name: CharField
        + email: CharField
        + location: CharField
        + about: TextField
        + route_types_offered: boolean[*]
        + membership_price: DecimalField
        + daily_price: DecimalField
        + get_absolute_url()
    }

    class Route {
        + level: IntegerField
        + route_setter: CharField
        + is_active: Boolean
        + date_added: DateField
        + about: TextField
        + wall_num: IntegerField
        + route_type: CharField
        + gym: Gym
        + get_absolute_url()

    }
