from __future__ import annotations
from sqlalchemy import ForeignKey
from spiffworkflow_backend.models.bpmn_process_definition import BpmnProcessDefinitionModel

from spiffworkflow_backend.models.db import db
from spiffworkflow_backend.models.db import SpiffworkflowBaseDBModel


# properties_json attributes:
#   "last_task", # guid generated by spiff
#   "root", # guid generated by spiff
#   "success", # boolean
#   "bpmn_messages", # if top-level process
#   "correlations", # if top-level process
class BpmnProcessModel(SpiffworkflowBaseDBModel):
    __tablename__ = "bpmn_process"
    id: int = db.Column(db.Integer, primary_key=True)

    parent_process_id: int = db.Column(ForeignKey("bpmn_process.id"), nullable=True)

    properties_json: dict = db.Column(db.JSON, nullable=False)
    json_data_hash: str = db.Column(db.String(255), nullable=False, index=True)

    # subprocess or top_level_process
    process_type: str = db.Column(db.String(30), nullable=False)
