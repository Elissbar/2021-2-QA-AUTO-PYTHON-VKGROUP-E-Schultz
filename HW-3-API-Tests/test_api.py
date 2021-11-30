from base import BaseCase
import pytest


@pytest.mark.API
class TestApi(BaseCase):
    authorize = True

    def test_create_campaign(self, post_create_campaign, file_path, fake_data):
        assert self.api_client.get_check_campaign(campaign_id=post_create_campaign)

    def test_create_segment(self, fake_data):
        id_segment = self.api_client.post_create_segment(segment_name=fake_data)
        assert self.api_client.get_check_segment(id_segment=id_segment)
        self.api_client.delete_delete_segment(id_segment=id_segment)

    def test_delete_segment(self, fake_data):
        id_segment = self.api_client.post_create_segment(segment_name=fake_data)
        self.api_client.delete_delete_segment(id_segment=id_segment)
        assert not self.api_client.get_check_segment(id_segment=id_segment)
