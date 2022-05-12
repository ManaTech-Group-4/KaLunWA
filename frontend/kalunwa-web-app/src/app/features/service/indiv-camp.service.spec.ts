import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';
import { CampEventModel, CampInfoModel, CampProjectModel } from '../models/campReqests/campRequests-model';

import { IndivCampService } from './indiv-camp.service';

  const mockInfo: CampInfoModel =
    {
      "id": 1,
      "name": "Lasang",
      "image": {id:1, image: "asdasda"},
      "gallery": [],
      "description": "asdfasdfasdf"
    };
  const mockEvents: CampEventModel[] =[
    {
      "id": 1,
      "title": "asdasdasd",
      "image": {id:1, image: "asdasda"}
    },
    {
      "id": 2,
      "title": "asdasdasd",
      "image": {id:1, image: "asdasda"}
    },
    {
      "id": 3,
      "title": "asdasdasd",
      "image": {id:1, image: "asdasda"}
    }
  ];
  const mockProjects: CampProjectModel[] =[
    {
      "id": 1,
      "title": "asdasdasd",
      "image": {id:1, image: "asdasda"}
    },
    {
      "id": 2,
      "title": "asdasdasd",
      "image": {id:1, image: "asdasda"}
    },
    {
      "id": 3,
      "title": "asdasdasd",
      "image": {id:1, image: "asdasda"}
    }
  ];

describe('IndivCampService', () => {
  let service: IndivCampService,
  httpTestingController: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [IndivCampService]
       });
    service = TestBed.inject(IndivCampService);
    httpTestingController = TestBed.get(HttpTestingController);
  });

  afterEach(()=>{
    httpTestingController.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });


  it('retrieve camp events from getCampEvents()', () => {

    service.getCampEvents("Lasang").subscribe((camps)=>{
      expect(mockEvents).toBe(camps,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/events/?expand=image&camp=Lasang&omit=created_at,updated_at,description,status,start_date,end_date,camp');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(mockEvents);

  });

  it('retrieve camp Projects from getCampProjects()', () => {

    service.getCampProjects("Lasang").subscribe((camps)=>{
      expect(mockProjects).toBe(camps,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/projects/?expand=image&camp=Lasang&omit=created_at,updated_at,description,status,start_date,end_date,camp');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(mockProjects);

  });

  it('retrieve camp Info from getCampInfo()', () => {

    service.getCampInfo(1).subscribe((camps)=>{
      expect(mockInfo).toBe(camps,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/camps/1/?expand=gallery,image&omit=camp_leader,created_at,updated_at');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(mockInfo);

  });

});
