var glancesApp = angular.module('glancesApp', ['ngRoute', 'glances.config', 'cfp.hotkeys'])

.value('CONFIG', {})
.value('ARGUMENTS', {})

.config(function(hotkeysProvider) {
  hotkeysProvider.useNgRoute = false;
  hotkeysProvider.includeCheatSheet = false;
})

.run(function($rootScope) {
      $rootScope.title = "Glances";
});
