import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';
import { EventsItemsModel } from '../models/event-items-model';
import { EventsResponseModel } from '../models/events-response-model';
import { IndivEventsModel } from '../models/indiv-event-model';

import { EventspageService } from './eventspage.service';
  const testEvents: EventsResponseModel[] = [
    {
        "id": 4,
        "title": "Event 4",
        "image":{"image": 'asda'},
        "description": "d",
        "start_date": "April 6, 2022",
        "end_date": "April 6, 2022",
        "camp": "Suba",
        "status": "Past"
    },
    {
        "id": 3,
        "title": "Event 3",
        "image":{"image": 'asda'},
        "description": "description 3",
        "start_date": "March 28, 2022",
        "end_date": "March 28, 2022",
        "camp": "General",
        "status": "Past"
    },
    {
        "id": 2,
        "title": "Event 2",
        "image":{"image": 'asda'},
        "description": "description 2",
        "start_date": "March 28, 2022",
        "end_date": "March 28, 2022",
        "camp": "General",
        "status": "Past"
    },
    {
        "id": 1,
        "title": "Event 1",
        "image":{"image": 'asda'},
        "description": "description 1",
        "start_date": "March 28, 2022",
        "end_date": "March 28, 2022",
        "camp": "General",
        "status": "Past"
    }
]
  const mockEvent: IndivEventsModel =
  {
      "id": 1,
      "title": "Event 1",
      "image":{"id": 1,"image": 'asda'},
      "description": "description 1",
      "start_date": "March 28, 2022",
      "end_date": "March 28, 2022",
      "camp": "General",
      "status": "Past",
      "gallery": [],
      "contributors": []
  }
describe('EventspageService', () => {
  let service: EventspageService,
  httpTestingController: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports : [ HttpClientTestingModule ]});
    service = TestBed.inject(EventspageService);
    httpTestingController = TestBed.get(HttpTestingController);
  });

  afterEach(()=>{
    httpTestingController.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('retrieve data from getEventList', () => {

    service.getEventList().subscribe((member)=>{
      expect(testEvents).toBe(member,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/events/?expand=image');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(testEvents);

  });


  it('retrieve data from getEventDetails', () => {

    service.getEventDetails("1").subscribe((member)=>{
      expect(mockEvent).toBe(member,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/events/1/?expand=image,contributors.image,gallery&omit=created_at,updated_at&query_limit_gallery=10');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(mockEvent);

  });
});
