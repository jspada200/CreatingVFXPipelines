from JPipe.base import JPipeBase

class DataManager(JPipeBase):

    def get_next_publish_version(self, entity: str, entity_type: str) -> int:
        """
        Get the next publish version for the provided publish dir.
        :param entity: The entity to get the next publish version for.
        :param entity_type: The type of entity to get the next publish version for (shot/asset/ext).
        :returns int: The next publish version.
        """
        raise NotImplementedError("Must implement in a derived class.")

    def write_publish_data(self,
                           publish_version: int,
                           entity: str,
                           entity_type:str,
                           publish_data: dict) -> None:
        """
        Write the publish data to the DB.
        :param publish_version: The version number to publish
        :param entity: The entity name to publish to
        :param entity_type: The type of entity we are publishing.
        :return:
        """
        raise NotImplementedError("Must implement in a derived class.")
