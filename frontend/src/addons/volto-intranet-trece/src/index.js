// Visoes
import AreaView from './components/View/AreaView';

const applyConfig = (config) => {
  config.settings = {
    ...config.settings,
    isMultilingual: false,
    supportedLanguages: ['pt-br'],
    defaultLanguage: 'pt-br',
  };
  config.views.contentTypesViews = {
    ...config.views.contentTypesViews,
    Area: AreaView,
  };
  return config;
};

export default applyConfig;
