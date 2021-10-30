from base import BaseCase
import pytest


@pytest.mark.API
class TestApi(BaseCase):
    authorize = True

    def test_create_campaign(self, file_path, fake_data):
        campaign_id = self.api_client.create_campaign(file_path=file_path, campaign_name=fake_data)
        assert self.api_client.check_campaign(campaign_id=campaign_id)
        self.api_client.delete_campaign(campaign_id=campaign_id)

    def test_create_segment(self, fake_data):
        id_segment = self.api_client.create_segment(segment_name=fake_data)
        assert self.api_client.check_segment(id_segment=id_segment)
        self.api_client.delete_segment(id_segment=id_segment)

    def test_delete_segment(self, fake_data):
        id_segment = self.api_client.create_segment(segment_name=fake_data)
        self.api_client.delete_segment(id_segment=id_segment)
        assert not self.api_client.check_segment(id_segment=id_segment)
