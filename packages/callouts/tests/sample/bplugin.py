import callouts 

@callouts.base
class BPlugin:
    def get_id() -> int:
        pass 

    @callouts.first
    def get_name() -> str:
        pass

    @callouts.flat
    def do_your_maths(*args) -> list:
        pass