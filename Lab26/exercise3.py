
class Microorganisms:
    def replicate(self):
        print('Not implemented')


class Bacteria(Microorganisms):
    def replicate(self):
        print('Replicates by fission')

class Virus(Microorganisms):
    def replicate(self):
        print('Replicates inside the host')




def replicate_organisms(organism):
    organism.replicate()


def main():
    micro = Microorganisms()
    virus = Virus()
    bacteria = Bacteria()
    replicate_organisms(micro)
    replicate_organisms(virus)
    replicate_organisms(bacteria)


if __name__ == "__main__":
    main()