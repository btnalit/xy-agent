from dataclasses import dataclass


@dataclass(slots=True)
class AuditRecord:
    actor: str
    action: str
    result: str
    evidence_path: str
