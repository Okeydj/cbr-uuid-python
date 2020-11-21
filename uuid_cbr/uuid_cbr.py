from .uuid_cbr_c import _uuid_cbr_c as uuuuid


def uuid():
    """
    Generate uuid cb rf
    """
    new_uuid = uuuuid.generate()
    if new_uuid is None or "":
        raise RuntimeError('Error uuid generation')
    return new_uuid
