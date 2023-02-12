<script>
export default {
  data() {
    return {
      PickupRequests: []
    };
  },
  created() {
    $.ajax({
      url: '/get_pickupRequests/',
      type: 'GET',
      dataType: 'json',
      success: (data) => {
        this.PickupRequest = data.PickupRequests;
      },
      error: (error) => {
        console.error(error);
      }
    });
  }
};
</script>