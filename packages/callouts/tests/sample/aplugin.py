import callouts

@callouts.base
class APlugin:
    def get_id() -> int: 
        return 0

    @callouts.first
    def get_name() -> str:
        pass

    def get_not_once_implemented() -> str:
        return 'default value'

    @callouts.flat 
    def get_many() -> list:
        pass