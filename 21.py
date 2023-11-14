class Clock:
    production_name = None
    production_id = None

    def clock_ring(self, *infos):
        self.production_name = infos[0]
        self.production_id = infos[1]
        import winsound
        print(f"name:{self.production_name},id:{self.production_id}")
        # winsound.Beep(3000, 1000)



clock1 = Clock()
clock1.clock_ring('gao', 130)
clock2 = Clock()
