function call_about(item_of_choice) {
    var params = {'item': item_of_choice, 'name': 'anonymous'};
    Twilio.Device.connect(params);
}