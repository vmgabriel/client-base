g// Definition control of javascript

// Composer
const compose = (...functions) => args => functions.reduceRight((arg, fn) => fn(arg), args);
const head = (data) => data[0];
const getItem = (value) => (data) => data[value];
const mapFunction = (func) => (elements) => elements.map(func);
const pushData = (data) => (arr) => {arr.push(data); return arr;};
const join = (separation) => (arr) => arr.join(separation);

const getElement = (data) => document.getElementById(data);
const getChildrenArray = (element) => [].slice.call(element.children);
const setClassIntoElement = (toClass) => (element) => {element.className = '';element.className = toClass;};

// Data: element of html
const getClasses = (data) => data.className;

// Separe a str converting to array and get active data
const isActiveClass = (state) =>(data) => {
  const re = new RegExp(state);
  const datas = data.split(" ");
  return datas.filter(word => re.exec(word)).length > 0;
};

const dropStateClass = (state) => (data) => {
  const re = new RegExp(state);
  const datas = data.split(" ");
  return datas.filter(word => !(re.exec(word)));
};

// Is Active Element
const isActiveClassElement =  compose(
  isActiveClass('sidebar-active'),
  getClasses,
  getElement,
);

const switchClassElement = (to_deactivate) => (to_activate) => compose(
  join(" "),
  pushData(to_activate),
  dropStateClass(to_deactivate),
  getClasses,
  getElement,
);

const getPElementBasedIntoItem = (visibility) => compose(
  setClassIntoElement(visibility),
  getItem(1),
  getChildrenArray,
  head,
  getChildrenArray,
  head,
  getChildrenArray,
);


function activateSidebar() {
  const sidebar = 'sidebar';
  const isActiveSidebar = isActiveClassElement(sidebar);

  // switch values of class to change
  const classVisibility = (isActiveSidebar) ? 'show' : 'hidden' ;
  const classSidebarActive = (isActiveSidebar) ? 'sidebar-inactive' : 'sidebar-active' ;
  const classSidebarInactive = (isActiveSidebar) ? 'sidebar-active' : 'sidebar-inactive' ;

  // Delete the elements P values of list
  const itemsElement = getElement('items-menu');
  let itemsMenu = getChildrenArray(itemsElement);
  itemsMenu = mapFunction(getPElementBasedIntoItem(classVisibility))(itemsMenu);

  // Activate or Deactivate the sidebar
  const classSidebarStep = switchClassElement(classSidebarInactive)(classSidebarActive)('sidebar');
  console.log('clasSidebarStep - ', classSidebarStep);
  setClassIntoElement(classSidebarStep)(getElement(sidebar));
};
