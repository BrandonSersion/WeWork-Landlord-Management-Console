(function() {
  'use strict';

  var app = angular.module('weWork', [])

    app.controller("WeWorkCtrl", function($http, $scope) {
      $http.get("./test_data/rooms.json").then(function (response) {
        $scope.rooms = response.data;

      });
    })

    app.controller("ReviewCtrl");

}());
