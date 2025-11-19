This repository is a small Python project for solving a vehicle routing / CVRP-style problem.

Guidance for AI coding agents working in this repo

- Purpose: Short exploration script (`main.py`) that contains data (clients, vehicle capacities, distance matrix) and a simple simulated annealing loop scaffold. Keep changes minimal and focused.

- Big picture:
  - `main.py` is the single entry point. It defines:
    - `clientes`: list of client demands (first element is depot 0)
    - `vehiculos`: list of vehicle capacities
    - `distancia_entre_clientes`: symmetric distance matrix between nodes
    - `solucion_inicial`: an ordering of visits used as a starting solution
    - a simulated annealing scaffold with `alpha`, `temp_inicial`, `temp_minima`, and `iteraciones_max`
  - No modules, packages, or tests currently exist. Any refactor should preserve the numerical data and the expected algorithmic intent (CVRP + simulated annealing).

- Project-specific conventions and patterns:
  - The code uses Spanish identifiers (`clientes`, `vehiculos`, `distancia_entre_clientes`, `solucion_inicial`). When adding functions or variables, prefer English only if you update all related names consistently — better to follow existing Spanish naming to keep readability for the repository owner.
  - Keep the data structures as plain Python lists/matrices; do not introduce heavy-weight dependencies for small changes.

- Developer workflows & commands:
  - Running: `python main.py` from the repository root (Windows PowerShell).
  - No build/test system present. Add `requirements.txt` only if new external packages are introduced.

- When modifying algorithm code:
  - Make changes incremental: add new helper functions (e.g., `evaluate_solution`, `neighbor`, `anneal_step`) in `main.py` or in a new module `cvrp.py` and update `main.py` to import them.
  - Keep printing limited to key progress indicators (temperature, best cost) so output remains readable.
  - Preserve the existing sample data when adding tests or examples. Use the arrays from `main.py` as canonical small-instance input.

- Integration points and dependencies:
  - Currently none external. If adding plotting or optimization libraries, document them in `requirements.txt`.

- Examples (copyable) to follow repository style:
  - Run the script: `python main.py`
  - Small refactor pattern: create `cvrp.py` with `def evaluate_solution(sol, distances, demands, capacities): ...` and import it in `main.py`.

- PR guidance for contributors (AI agents):
  - Keep changes focused to a single concern per PR (refactor, add heuristic, or add tests).
  - Add or update `README.md` if you add new files or change the run instructions.

If anything here is unclear or you want more detail (example functions, suggested tests, or a small refactor to a `cvrp.py` module), tell me which direction you prefer and I'll update the instructions accordingly.
