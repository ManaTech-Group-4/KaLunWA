export module homepageInfo {

  export interface Image {
      id: number;
      image: string;
  }

  export interface Event {
      id: number;
      title: string;
      image: Image;
      description: string;
      start_date: Date;
      end_date: Date;
      camp: string;
      created_at: Date;
      updated_at: Date;
      status: string;
  }

  export interface PageContainedEvent {
      id: number;
      container: number;
      event: Event;
      section_order: number;
  }


  export interface Jumbotron {
      id: number;
      header_title: string;
      subtitle: string;
      image: Image;
      created_at: Date;
      updated_at: Date;
  }

  export interface PageContainedJumbotron {
      id: number;
      container: number;
      jumbotron: Jumbotron;
      section_order: number;
  }


  export interface Project {
      id: number;
      title: string;
      image: Image;
      description: string;
      start_date: Date;
      end_date: Date;
      camp: string;
      created_at: Date;
      updated_at: Date;
      status: string;
  }

  export interface PageContainedProject {
      id: number;
      container: number;
      project: Project;
      section_order: number;
  }

  export interface HomepageContainer {
      id: number;
      name: string;
      slug: string;
      page_contained_events: PageContainedEvent[];
      page_contained_jumbotrons: PageContainedJumbotron[];
      page_contained_projects: PageContainedProject[];
  }

}
