import hug
import nameko
import uuid

# todo: move uuid.hex to utlis function?
# see: https://stackoverflow.com/questions/36588126/uuid-is-not-json-serializable

@hug.get('/getCandidateSkill', versions=1)
def getCandidateSkill():
    """Returns a candidate skill object for labeling."""
    candidate = "<insert skill>"
    context = "<context>"
    # this should be a utils function
    candidate_uuid = uuid.uuid5(uuid.NAMESPACE_DNS,
                                candidate+context)
    return {"candidate": candidate,
            "context": context,
            "uuid": candidate_uuid.hex}

@hug.put('/putCandidateSkill', versions=1)
def putCandidateSkill(uuid: hug.types.uuid, label: hug.types.boolean):
    """Accepts a candidate uuid, label"""
    return {"uuid": uuid.hex,
            "label": label}
