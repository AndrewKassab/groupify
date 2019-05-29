SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: ar_internal_metadata; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ar_internal_metadata (
    key character varying NOT NULL,
    value character varying,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


--
-- Name: auth_tokens; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_tokens (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    token character varying NOT NULL
);


--
-- Name: auth_tokens_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_tokens_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_tokens_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_tokens_id_seq OWNED BY public.auth_tokens.id;


--
-- Name: group_users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.group_users (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    user_id integer NOT NULL
);


--
-- Name: group_users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.group_users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: group_users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.group_users_id_seq OWNED BY public.group_users.id;


--
-- Name: groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    title character varying NOT NULL
);


--
-- Name: groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.groups_id_seq OWNED BY public.groups.id;


--
-- Name: schema_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.schema_migrations (
    version character varying NOT NULL
);


--
-- Name: spotify_playlists; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.spotify_playlists (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    user_id integer NOT NULL,
    spotify_id character varying
);


--
-- Name: spotify_playlists_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.spotify_playlists_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: spotify_playlists_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.spotify_playlists_id_seq OWNED BY public.spotify_playlists.id;


--
-- Name: tracks; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tracks (
    id bigint NOT NULL,
    name character varying,
    duration integer,
    spotify_id character varying,
    group_id integer,
    rank integer,
    artists character varying
);


--
-- Name: tracks_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.tracks_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: tracks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.tracks_id_seq OWNED BY public.tracks.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    name character varying NOT NULL,
    spotify_id character varying,
    access_token character varying,
    refresh_token character varying,
    token_expiration timestamp without time zone,
    username character varying
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: auth_tokens id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_tokens ALTER COLUMN id SET DEFAULT nextval('public.auth_tokens_id_seq'::regclass);


--
-- Name: group_users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_users ALTER COLUMN id SET DEFAULT nextval('public.group_users_id_seq'::regclass);


--
-- Name: groups id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.groups ALTER COLUMN id SET DEFAULT nextval('public.groups_id_seq'::regclass);


--
-- Name: spotify_playlists id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.spotify_playlists ALTER COLUMN id SET DEFAULT nextval('public.spotify_playlists_id_seq'::regclass);


--
-- Name: tracks id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tracks ALTER COLUMN id SET DEFAULT nextval('public.tracks_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: ar_internal_metadata ar_internal_metadata_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ar_internal_metadata
    ADD CONSTRAINT ar_internal_metadata_pkey PRIMARY KEY (key);


--
-- Name: auth_tokens auth_tokens_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_tokens
    ADD CONSTRAINT auth_tokens_pkey PRIMARY KEY (id);


--
-- Name: group_users group_users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_users
    ADD CONSTRAINT group_users_pkey PRIMARY KEY (id);


--
-- Name: groups groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (id);


--
-- Name: schema_migrations schema_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.schema_migrations
    ADD CONSTRAINT schema_migrations_pkey PRIMARY KEY (version);


--
-- Name: spotify_playlists spotify_playlists_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.spotify_playlists
    ADD CONSTRAINT spotify_playlists_pkey PRIMARY KEY (id);


--
-- Name: tracks tracks_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tracks
    ADD CONSTRAINT tracks_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: index_auth_tokens_on_token; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_auth_tokens_on_token ON public.auth_tokens USING btree (token);


--
-- Name: index_auth_tokens_on_user_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_auth_tokens_on_user_id ON public.auth_tokens USING btree (user_id);


--
-- Name: index_group_users_on_group_id_and_user_id; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX index_group_users_on_group_id_and_user_id ON public.group_users USING btree (group_id, user_id);


--
-- Name: index_group_users_on_user_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_group_users_on_user_id ON public.group_users USING btree (user_id);


--
-- Name: index_groups_on_user_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_groups_on_user_id ON public.groups USING btree (user_id);


--
-- Name: index_spotify_playlists_on_group_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_spotify_playlists_on_group_id ON public.spotify_playlists USING btree (group_id);


--
-- Name: index_spotify_playlists_on_user_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_spotify_playlists_on_user_id ON public.spotify_playlists USING btree (user_id);


--
-- Name: index_tracks_on_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_tracks_on_name ON public.tracks USING btree (name);


--
-- Name: index_tracks_on_spotify_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_tracks_on_spotify_id ON public.tracks USING btree (spotify_id);


--
-- Name: auth_tokens fk_rails_0d66c22f4c; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_tokens
    ADD CONSTRAINT fk_rails_0d66c22f4c FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: group_users fk_rails_1486913327; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_users
    ADD CONSTRAINT fk_rails_1486913327 FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: groups fk_rails_5e78cd340a; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT fk_rails_5e78cd340a FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: spotify_playlists fk_rails_7241dcf17c; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.spotify_playlists
    ADD CONSTRAINT fk_rails_7241dcf17c FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: group_users fk_rails_a9d5f48449; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_users
    ADD CONSTRAINT fk_rails_a9d5f48449 FOREIGN KEY (group_id) REFERENCES public.groups(id);


--
-- Name: spotify_playlists fk_rails_bd6209a3bc; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.spotify_playlists
    ADD CONSTRAINT fk_rails_bd6209a3bc FOREIGN KEY (group_id) REFERENCES public.groups(id);


--
-- PostgreSQL database dump complete
--

SET search_path TO "$user", public;

INSERT INTO "schema_migrations" (version) VALUES
('20190425233315'),
('20190503000150'),
('20190504085846'),
('20190506201347'),
('20190509235700'),
('20190510001300'),
('20190517010956');


